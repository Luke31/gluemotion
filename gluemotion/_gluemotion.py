class Gluemotion:
    def __init__(self, text_col):
        """

        :param text_col: column-name which contains text to anaylyze
        """
        super().__init__()
        self.text_col = text_col

    def add_covid_check(self, rec):
        """
        Analyze Text in AWS Glue DynamicFrame.

        Adds following columns to the DynamicFrame:
        - covid_mentioned e.g. True if text contains 'covid', else False

        :param rec: DyanmicFrame to expand with covid_mentioned
        :return: new dynamicFrame containing original text and new covid_mentioned-col
        """
        has_covid = 'covid' in rec[self.text_col].lower()
        rec["text"] = rec[self.text_col]
        rec["covid_mentioned"] = has_covid
        return rec
