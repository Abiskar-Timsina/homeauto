import random


class Token:
    def __init__(self,length:int = 64) -> None:
        self.length = length
    
    def gen_token(self) -> str:
        """
        This method returns a alphanumeric token of specified length (64)

        Params:

        None

        Returns:

        str
        
        """

        token_ = str()

        while len(token_) < self.length:
            code = random.randint(48,122)
            temp_ = chr(code)

            if temp_.isalnum():
                token_ += temp_
        
        return token_