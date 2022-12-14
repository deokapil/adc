const fetchData = async (
  { url, method = "POST", token = "", body = null },
  dispatch
) => {
  const headers = token
    ? { "Content-Type": "application/json", authorization: `Token ${token}` }
    : { "Content-Type": "application/json" };
  body = body ? { body: JSON.stringify(body) } : {};
  try {
    const response = await fetch(url, { method, headers, ...body });
    const data = await response.json();
    if (response.status === 401) {
      dispatch({ type: "UPDATE_USER", payload: null });
      throw new Error("User has been logged out");
    }
    return data;
  } catch (error) {
    dispatch({
      type: "UPDATE_ALERT",
      payload: { open: true, severity: "error", message: error.message },
    });
    return null;
  }
};

export default fetchData;
