import pvporcupine
import pvrhino
import json
from pvrecorder import PvRecorder
from datetime import datetime
from assistant.fixyou import FixYou


class Assistant:
    def __init__(self) -> None:
        with open("./env.json", "r") as f:
            env = json.load(f)

        self.porcupine = pvporcupine.create(
            access_key=env["access_key"],
            keywords=['porcupine']
        )

        self.rhino = pvrhino.create(
            access_key=env["access_key"],
            context_path=env["context_path"]
        )

        # Device Helper
        # devices = PvRecorder.get_audio_devices()
        # print(devices)

        # porcupine and rhino have the same frame_length
        # So they are interchangable
        self.recorder = PvRecorder(
            device_index=1,
            frame_length=self.porcupine.frame_length)
        
        self.fixyou = FixYou()

    def active_listening(self):
        try:
            while True:
                pcm = self.recorder.read()

                is_finalized = self.rhino.process(pcm)
                if is_finalized:
                    inference = self.rhino.get_inference()
                    if inference.is_understood:
                        print(inference.intent)
                        self.fixyou.toggle(inference.intent)
                    else:
                        print("I don't understand")
                    # After we process the command we break out
                    # of active listening.
                    break
        except:
            print("Active listening is now stopping.")
        finally:
            pass

    def run_loop(self):
        '''
        This is the loop that will listen for wake
        words. It will call a different function
        when it wakes up.
        '''
        self.recorder.start()

        try:
            while True:
                pcm = self.recorder.read()
                result = self.porcupine.process(pcm)

                if result >= 0:
                    print(f"{datetime.now()} - I have been awakened!")
                    self.active_listening()
        except:
            print("Run loop is now quitting.")
        finally:
            self.recorder.delete()
            self.porcupine.delete()
            self.rhino.delete()


if __name__ == '__main__':
    assistant = Assistant()
    assistant.run_loop()
