import "./About.css";
import { AnimatedScroll } from "./widgets/AnimatedScroll";
import { MainInfo } from "./widgets/MainInfo";
import { Certificate } from "./widgets/Certificate";

export function About() {
  return (
    <section className="infocont">
      <AnimatedScroll />
      <MainInfo />
      <section>
        <h2>Video about us</h2>
        <video
          width="600"
          height="340"
          controls
          muted
          poster="/about/poster.jpg"
        >
          <source src="/about/about.mp4" type="video/mp4" />
          Ваш браузер не поддерживает видео.
        </video>
      </section>
      <section className="hist-req-sec">
        <section>
          <h2>Our history</h2>
          <pre className="history">
            {`2020: Открытие первого магазина\n2021: Запуск интернет-магазина\n2022: Расширение ассортимента книг и штата сотрудников\n2023: Открытие новых магазинов в соседних странах\n2024: Новые партнёры и огромные инвестиции в проект`}
          </pre>
        </section>
        <section>
          <h2>Shop requisites</h2>
          <pre>
            {`ИНН: 1337228007\nОГРН: 9876543211234\nКПП: 543210001\nЮридическийадрес: г. Минск, ул. Литературная, д. 10\nБанк: ПАО "GOsling Bank"\nБИК: 044525225 Расчетный счет: 40702810500000098765`}
          </pre>
        </section>
      </section>
      <Certificate />
    </section>
  );
}
