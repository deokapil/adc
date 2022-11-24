import fetchData from "./utils/fetchData";

const url = "http://localhost:8000/api/";

export const login = async (user, dispatch) => {
  dispatch({ type: "START_LOADING" });

  const result = await fetchData(
    { url: url + "auth/login", body: { user } },
    dispatch
  );
  if (result?.user) {
    dispatch({ type: "UPDATE_USER", payload: result.user });
    dispatch({ type: "CLOSE_LOGIN" });
  }
  if (result?.errors) {
    dispatch({
      type: "UPDATE_ALERT",
      payload: { open: true, severity: "error", message: result?.errors[0] },
    });
  }

  dispatch({ type: "END_LOADING" });
};
