import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { createRoot } from 'react-dom/client'

import './index.css'
import Cadastro from './pages/Cadastro'
import { AuthProvider } from './contexts/AuthContext'
import HomeGestor from './pages/HomeGestor'
import LandPage from './pages/LandPage'


createRoot(document.getElementById('root')).render(
  <AuthProvider>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<LandPage/>}/>
        <Route path='/cadastro' element={<Cadastro/>} />
        <Route path='/homeGestor' element={<HomeGestor/>} />
      </Routes>
    </BrowserRouter>,
  </AuthProvider>
)
