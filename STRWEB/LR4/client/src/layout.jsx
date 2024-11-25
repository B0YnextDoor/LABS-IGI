import { Sidebar } from "./components/sidebar/Sidebar.jsx";
import { Header } from "./components/header/Header.jsx";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { Toaster } from "sonner";

const client = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
    },
  },
});

function Layout(props) {
  return (
    <QueryClientProvider client={client}>
      <section className="layout">
        <Sidebar />
        <section className="layout-content">
          <Header />
          {props.children}
        </section>
        <Toaster
          position="top-center"
          closeButton={true}
          richColors={true}
          gap={8}
          toastOptions={{ duration: 3000 }}
        />
      </section>
    </QueryClientProvider>
  );
}

export default Layout;
