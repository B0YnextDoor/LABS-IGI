import { useEffect, useState } from "react";
import { apiService } from "../../../services/api.service";
import { Loader } from "../../../components/loader/Loader";
import styles from "../Home.module.css";

export const ApiSection = () => {
  const [poem, setPoem] = useState(null);
  const [fact, setFact] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [poemData, factData] = await Promise.all([
          apiService.getPoem(),
          apiService.getFact(),
        ]);
        console.log(poemData);
        console.log(factData);
        setPoem(poemData);
        setFact(factData);
      } catch (err) {
        console.error("Ошибка при получении данных:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);
  if (loading) return <Loader />;
  return (
    <div className={styles.api_cont}>
      {fact?.text && (
        <div>
          <h2>Fact of the day:</h2>
          <p>{fact.text}</p>
          {fact.source && (
            <div>
              <a href={fact.source} className="animated-link">
                Source
              </a>
            </div>
          )}
        </div>
      )}
      {poem?.title && (
        <div>
          <h2>{poem.title}</h2>
          <h3>Author: {poem.author}</h3>
          <pre>{poem?.lines && poem.lines.join("\n")}</pre>
        </div>
      )}
    </div>
  );
};
