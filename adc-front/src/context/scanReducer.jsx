const scanReducer = (state, action) => {
  switch (action.type) {
    case "ADD_TO_LIST":
      return {
        ...state,
        scannedList: [action.payload, ...state.scannedList],
      };
    case "EMPTY_LIST":
      return { ...state, scannedList: [] };
    case "RESET_SESSION":
      return { ...state, sessionId: null, scannedList: [] };
    case "NEW_SESSION":
      return { ...state, sessionId: action.payload };
    case "NEXT_SESSION":
      return { ...state, sessionId: null, scannedList: [] };
    default:
      throw new Error("No matched action!");
  }
};

export default scanReducer;
