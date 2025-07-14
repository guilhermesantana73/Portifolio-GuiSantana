import { createContext, useState, useEffect, useContext } from "react"

export const AuthContext = createContext(null)

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState('')
    const [token, setToken] = useState('')
    const [loading, setLoading] = useState(true)

    useEffect(()=> {
        const tokenGuardado = localStorage.getItem('authToken')
        const usuarioLogado = localStorage.getItem('authUser')

        if (tokenGuardado && usuarioLogado) {
            try {
                setUser(JSON.parse(usuarioLogado))
                setToken(tokenGuardado)
            } catch (e) {
                console.log('Erro no usuário ou token no localStorage', e)
                logout()
            }
        }
        setLoading(false)
    }, [])

    const login = (dadosUsuario, authToken) => {
        setUser(dadosUsuario)
        setToken(authToken)
        localStorage.setItem('authToken', authToken)
        localStorage.setItem('authUser', JSON.stringify(dadosUsuario))
    }

    const logout = () => {
        setUser(null)
        setToken(null)
        localStorage.removeItem('authToken')
        localStorage.removeItem('authUser')
    }

    const value = {
        user,
        token,
        loading,
        isAuthenticated: !!user && !!token,
        login,
        logout
    }

    return (
        <AuthContext.Provider value={value}>
            {loading ? (
                <div className='flex justify-center align-center h-screen text-1.5 text-[#333]'>
                    Carregando autenticação...
                </div>
            ) : (
                children
            )}
        </AuthContext.Provider>
    )
}

export const useAuth = () => {
    return useContext(AuthContext)
}