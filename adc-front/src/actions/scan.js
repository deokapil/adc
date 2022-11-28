import fetchData from "./utils/fetchData";

export const scanSubmit = async (
  scanId,
  sessionId,
  dispatch,
  listDispatch,
  currentUser
) => {
  dispatch({ type: "START_LOADING" });
  const result = await fetchData(
    {
      url: `${
        import.meta.env.VITE_APP_SERVER_URL
      }/operations/${sessionId}/entries`,
      body: {
        entry: {
          info: scanId,
        },
      },
      token: currentUser?.token,
    },
    dispatch
  );
  if (result?.entry) {
    listDispatch({ type: "ADD_TO_LIST", payload: result.entry });
  }
  if (result?.errors) {
    dispatch({
      type: "UPDATE_ALERT",
      payload: { open: true, severity: "error", message: result?.errors[0] },
    });
  }

  dispatch({ type: "END_LOADING" });
};

export const createSession = async (dispatch, listDispatch, currentUser) => {
  dispatch({ type: "START_LOADING" });
  const result = await fetchData(
    {
      url: `${import.meta.env.VITE_APP_SERVER_URL}/operations`,
      body: {},
      token: currentUser?.token,
    },
    dispatch
  );
  if (result?.operation) {
    await listDispatch({
      type: "NEW_SESSION",
      payload: result.operation.sessId,
    });
  }
  if (result?.errors) {
    dispatch({
      type: "UPDATE_ALERT",
      payload: { open: true, severity: "error", message: result?.errors[0] },
    });
  }
  dispatch({ type: "END_LOADING" });
  return result.operation.sessId;
};

export const createSession = async (dispatch, listDispatch, currentUser) => {
  dispatch({ type: "START_LOADING" });
  const result = await fetchData(
    {
      url: `${import.meta.env.VITE_APP_SERVER_URL}/operations`,
      body: {},
      token: currentUser?.token,
    },
    dispatch
  );
  if (result?.operation) {
    await listDispatch({
      type: "NEW_SESSION",
      payload: result.operation.sessId,
    });
  }
  if (result?.errors) {
    dispatch({
      type: "UPDATE_ALERT",
      payload: { open: true, severity: "error", message: result?.errors[0] },
    });
  }
  dispatch({ type: "END_LOADING" });
  return result.operation.sessId;
};
