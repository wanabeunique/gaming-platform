import { createSlice, PayloadAction } from '@reduxjs/toolkit'

type isAuthState = {
  data: false
}

const initialState: isAuthState = {
  data: false,
}

export const isAuthSlice = createSlice({
  name: 'isAuth',
  initialState,
  reducers: {
    setIsAuth(state, action: PayloadAction<boolean>) {
      state.data = action.payload;
    },
  }
});


export const { setIsAuth } = isAuthSlice.actions
export default isAuthSlice.reducer;