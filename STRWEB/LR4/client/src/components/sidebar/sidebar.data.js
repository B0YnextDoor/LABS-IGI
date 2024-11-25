import { LibraryBig, BadgeInfo, Star, Newspaper, Contact2 } from "lucide-react";
import { PAGES } from "../../config/routes";

export const MENU = [
  {
    link: PAGES.NEWS,
    name: "News",
    icon: Newspaper,
  },
  {
    link: PAGES.CATALOG,
    name: "Catalog",
    icon: LibraryBig,
  },
  {
    link: PAGES.REVIEWS,
    name: "Reviews",
    icon: Star,
  },
  {
    link: PAGES.EMPLOYEES,
    name: "Contacts",
    icon: Contact2,
  },
  {
    link: PAGES.ABOUT,
    name: "About",
    icon: BadgeInfo,
  },
];
