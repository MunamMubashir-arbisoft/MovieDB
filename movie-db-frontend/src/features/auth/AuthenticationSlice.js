import { createSlice } from '@reduxjs/toolkit'

export const auth = createSlice({
    name: 'auth',
    initialState: {
        isAuthenticated: false
    },
    reducers: {
        authenticateUser: (state) => {
            state.isAuthenticated = true
        },
        logOutUser: (state) => {
            state.isAuthenticated = false
        }

    },

})

export const { authenticateUser, logOutUser } = auth.actions;
export const selectAuthState = (state) => state.auth.isAuthenticated
export default auth.reducer;
