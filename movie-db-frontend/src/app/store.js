
import { configureStore } from '@reduxjs/toolkit'
import { reducer as formReducer } from 'redux-form'
import movieReducer from '../features/movies/MovieSlice'
import authReducer from '../features/auth/AuthenticationSlice'
import { createLogger } from 'redux-logger'
import thunkMiddleware from 'redux-thunk'

const loggerMiddleware = createLogger()

export const store = configureStore({
  reducer: {
    form: formReducer,
    movie: movieReducer,
    auth: authReducer
  },
  middleware: [thunkMiddleware, loggerMiddleware]
});