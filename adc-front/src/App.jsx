import Dashboard from "./pages/dashboard/Dashboard";
import Loading from "./components/Loading";
import Notification from "./components/Notification";
import ContextProvider from "./context/ContextProvider";

const App = () => {
  return (
    <>
      <ContextProvider>
        <Loading />
        <Notification />
        <Dashboard />
      </ContextProvider>
    </>
  );
};

export default App;
