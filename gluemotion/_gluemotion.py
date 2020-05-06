from mlask import MLAsk


class Gluemotion:
    def __init__(self, text_col) -> None:
        """

        :param text_col: column-name which contains text to anaylyze
        """
        super().__init__()
        self.text_col = text_col
        self.emotion_analyzer = MLAsk()

    def add_emotions(self, rec):
        """
        Analyze Text in AWS Glue DynamicFrame.

        Adds following columns to the DynamicFrame:
        - orientation e.g. positive, mostly positive, negative...
        - emotion_representative most relevant of e.g. 'yorokobi'
        - emotion_all list of recognised emotions e.g. ['yorokobi', 'suki']
        - emoticon list of recognised emoticons e.g. ['(;´Д`)']

        :param rec: DyanmicFrame to expand with emotion
        :return: new dynamicFrame containing original text and new emotion-col
        """
        result = self.emotion_analyzer.analyze(rec[self.text_col])
        rec["text"] = rec[self.text_col]
        rec["orientation"] = result['orientation']
        rec["emotion_representative"] = result['representative'][0]
        rec["emotion_all"] = [emotion for emotion in result['emotion']]
        rec["emoticons"] = result['emoticon']
        return rec
