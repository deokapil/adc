import React, { createContext, useContext, useReducer } from "react";
import scanReducer from "./scanReducer";

const ScanContext = createContext();

const initState = {
  scannedList: [],
  sessionId: null,
};

export function ScanProvider({ children }) {
  const [state, dispatch] = useReducer(scanReducer, initState);
  return (
    <ScanContext.Provider value={{ state, dispatch }}>
      {children}
    </ScanContext.Provider>
  );
}

export const useScanList = () => {
  return useContext(ScanContext);
};

export default ScanContext;
