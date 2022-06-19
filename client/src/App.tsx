import { Route, Routes } from "react-router-dom";
import { ToastContainer } from "react-toastify";

import Nav from "./components/Navs/Nav";
import "react-toastify/dist/ReactToastify.css";
import Home from "./pages/Home/Home";
import ChatPage from "./pages/ChatPage/ChatPage";
import FeedbackPage from "./pages/Feedback/FeedbackPage";

const App: React.FC = () => {
  const routes = (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/chat" element={<ChatPage />} />
      <Route path="/feedback" element={<FeedbackPage />} />
    </Routes>
  );
  return (
    <>
      <ToastContainer position="top-center" />
      <Nav />
      {routes}
    </>
  );
};

export default App;
