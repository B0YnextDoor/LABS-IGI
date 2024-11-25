import "./Animation.css";

export function Animation() {
  return (
    <div
      style={{
        width: "100%",
        display: "flex",
        flexDirection: "column",
        gap: "10px",
        alignItems: "center",
      }}
    >
      <h1 className="company-name">BOOKSHOP BOOKY</h1>
      <section className="anim-cont">
        <div className="book">
          <div className="cover">
            <img
              src="about/logo.jpg"
              alt="book cover"
              width="150"
              height="150"
            />
          </div>
          <div className="page"></div>
          <div className="page"></div>
          <div className="page"></div>
          <div className="page">
            <div className="page1">
              <div className="content content1">
                <div className="image img1"></div>
                <h2>Lorem Ipsum</h2>
                <p>
                  It is simply dummy text of the printing and typesetting
                  industry.
                </p>
              </div>
            </div>
          </div>
          <div className="page">
            <div className="page2">
              <div className="content content2">
                <div className="image img2"></div>
                <h2>Shrek</h2>
                <p>
                  Ogres are like an onions! End of story! Bye-bye! See ya
                  later...
                </p>
              </div>
              <div className="content content3">
                <div className="image img3"></div>
                <h2>Kitty</h2>
                <p>
                  I'm fine,
                  <br />
                  just trust me.
                </p>
              </div>
            </div>
          </div>
          <div className="page page4">
            <div className="content content4">
              <div className="image img4"></div>
              <h2>Piece of wisdom</h2>
              <p style={{ paddingInline: "5px" }}>
                I've finished a Numerical Analisis Methods course
                <br /> and wish every man to finish it.
              </p>
            </div>
          </div>
          <div className="back-cover"></div>
        </div>
      </section>
    </div>
  );
}
