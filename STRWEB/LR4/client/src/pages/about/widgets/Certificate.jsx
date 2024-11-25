export const Certificate = () => {
  return (
    <section>
      <h2>Certificate</h2>
      <article className="certificate-cont">
        <div className="certificate-border"></div>
        <div className="certificate-logo"></div>
        <section className="certificate-head">
          <h3>ЕДИНЫЙ РЕЕСТР МАГАЗИНОВ</h3>
          <h2>СВИДЕТЕЛЬСТВО</h2>
          <h3>
            <small>о внесении сведений</small>
          </h3>
        </section>
        <section className="certificate-body">
          <section>
            <div>г. Минск</div> <div>15 августа 2020 года</div>
          </section>
          <h3>
            Общество с ограниченной ответственностью{" "}
            <em>&laquo;BOOKY&raquo;</em>
          </h3>
          <p>(ИНН 1337228007)</p>
          <h3 className="undr">Сертификат №5678</h3>
        </section>
        <section className="certificate-footer">
          <section>
            <p>Важный Х.Б.</p>
            <p>Директор Ассоциации "ЛИТЕРАТОРЫ"</p>
          </section>
          <div className="stamp"></div>
          <hr />
          <section className="btm">
            <div className="certificate-logo small-logo"></div>
            <section>
              Ассоциация "Объединение книжных магазинов мира
              &laquo;ЛИТЕРАТОРЫ&raquo;"
              <br />
              123456 г. Минск, ул. Литературная д.10
              <br />
              Тел. +375331234567
              <br />
              literature@gmail.com
              <br />
            </section>
          </section>
        </section>
      </article>
    </section>
  );
};
