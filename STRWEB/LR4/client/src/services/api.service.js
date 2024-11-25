export const apiService = {
  POEM_URL: "https://poetrydb.org/title/Sonnet%2018",
  FACT_URL: "https://uselessfacts.jsph.pl/api/v2/facts/today",

  async getPoem() {
    const response = await fetch(this.POEM_URL).then((response) =>
      response.json()
    );
    if (response)
      return {
        author: response[0].author,
        title: response[0].title,
        lines: response[0].lines,
      };
    return {};
  },

  async getFact() {
    const response = await fetch(this.FACT_URL).then((response) =>
      response.json()
    );
    if (response)
      return {
        text: response.text,
        source: response.source_url,
      };
    return {};
  },
};
