import { Outlet } from "react-router-dom";
import Header from "../Header/Header";
import Footer from "../Footer/Footer";
import Friends from "../Friends/Friends";
import Menu from "../Menu/Menu";
import { useAppSelector } from "../../hooks";

export default function Layout() {
  const isAuth = useAppSelector((state) => state.authReducer.data);

  return (
    <div className="wrapper">
      <Header />
      <Outlet />
      {isAuth ? <Friends /> : null}
      {isAuth ? <Menu /> : null}
      <Footer />
    </div>
  );
}
