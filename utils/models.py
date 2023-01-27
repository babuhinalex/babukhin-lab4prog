from pydantic import BaseModel


class QuoteResponse(BaseModel):
    id: int
    quote: str
    author: str
    series: str

    def __str__(self):
        return f'''Series: {self.series}
Quote: {self.quote}
Author: ___{self.author}___
        '''
