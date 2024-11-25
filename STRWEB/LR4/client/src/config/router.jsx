import { PAGES } from "./routes";
import { Home } from "../pages/home/Home";
import { Catalog } from "../pages/catalog/Catalog";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Layout from "../layout";
import { SignIn } from "../pages/auth/SignIn";
import { SignUp } from "../pages/auth/SignUp";
import { Account } from "../pages/account/Account";
import { Book } from "../pages/catalog/Book";
import { BookForm } from "../pages/catalog/BookForm";
import { Cart } from "../pages/cart/Cart";
import { Order } from "../pages/order/Order";
import { Orders } from "../pages/order/Orders";
import { About } from "../pages/about/About";
import { Reviews } from "../pages/review/Reviews";
import { Review } from "../pages/review/Review";
import { News } from "../pages/news/News";
import { NewsDetail } from "../pages/news/NewsDetail";
import { NewsForm } from "../pages/news/NewsForm";
import { Contacts } from "../pages/contacts/Contacts";
import { Contact } from "../pages/contacts/Contact";

export const Router = () => {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          {routes.map((item) => (
            <Route key={item.path} path={item.path} element={item.element} />
          ))}
        </Routes>
      </Layout>
    </BrowserRouter>
  );
};

const routes = [
  {
    path: "sign-in",
    element: <SignIn />,
  },
  {
    path: "sign-up",
    element: <SignUp />,
  },
  {
    path: PAGES.HOME,
    element: <Home />,
  },
  {
    path: PAGES.CATALOG,
    element: <Catalog />,
  },
  {
    path: `${PAGES.CATALOG}/:id`,
    element: <Book />,
  },
  {
    path: `${PAGES.BOOK_FORM}/:upd?`,
    element: <BookForm />,
  },
  {
    path: PAGES.ACCOUNT,
    element: <Account />,
  },
  {
    path: PAGES.CART,
    element: <Cart />,
  },
  {
    path: `${PAGES.ORDER}/:id?`,
    element: <Order />,
  },
  {
    path: PAGES.ORDERS,
    element: <Orders />,
  },
  {
    path: PAGES.ABOUT,
    element: <About />,
  },
  {
    path: PAGES.REVIEWS,
    element: <Reviews />,
  },
  {
    path: `${PAGES.REVIEW}/:id?`,
    element: <Review />,
  },
  {
    path: PAGES.NEWS,
    element: <News />,
  },
  {
    path: `${PAGES.NEWS}/:id`,
    element: <NewsDetail />,
  },
  {
    path: `${PAGES.NEWS_FORM}/:id?`,
    element: <NewsForm />,
  },
  {
    path: PAGES.EMPLOYEES,
    element: <Contacts />,
  },
  {
    path: `${PAGES.EMPLOYEE_FORM}/:id`,
    element: <Contact />,
  },
];
