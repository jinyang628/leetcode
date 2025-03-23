from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        num_bulls = 0
        cow_secret_track = defaultdict(int)
        cow_guess_track = defaultdict(int)
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                num_bulls += 1
            else:
                cow_secret_track[secret[i]] += 1
                cow_guess_track[guess[i]] += 1
        num_cows = 0
        for key, value in cow_guess_track.items():
            num_cows += min(value, cow_secret_track[key])
        return f"{num_bulls}A{num_cows}B"