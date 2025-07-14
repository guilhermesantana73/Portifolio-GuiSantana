import './style.css'
import landingImg from '../assets/landing-photo.png'
import logo from '../assets/redLogo.svg'
import bgLight from '../assets/background-light.png'
import Input from '../components/Input'
import Button from '../components/Button'
import { useState} from 'react'
import { useAuth } from '../contexts/AuthContext'
import { useNavigate } from 'react-router-dom'

//pagina inicial
const LandPage = () => {
    const [email, setEmail] = useState('') //variavel para campo email
    const [password, setPassword] = useState('')
    const navigate = useNavigate()
    
    const { login, isAuthenticated, user} = useAuth()

    const handleSubmit = async (e) => {
        e.preventDefault()

        try {
            const res = await fetch('http://xyz/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password }),
            })

            const data = await res.json()

            if (res.ok) {
                login(data.user, data.token)
                if (isAuthenticated) redirect(user.role)
            }
        } catch (e) {
            console.error('Erro na requisição:', e)
        }
    }

    const redirect = (userType) => {
        switch (userType) {
            case 'gestor':
                navigate('/homeGestor')
                break
            case 'doador':
                navigate('/homeDoador')
                break
            case 'admin':
                navigate('/homeAdmin')
                break
            default:
                break
        }
    }


    return (
        <div className='w-screen h-screen flex justify-center items-center sm:p-0' style={{ backgroundImage: `url(${bgLight})`, backgroundSize: 'cover', backgroundBlendMode: 'overlay', backgroundPosition: 'center' }}>
            <div className='m-auto p-3 bg-[#d9d9d9] rounded-2xl min-w-[240px]  w-[50vw] min-h-[350px] h-auto lg:h-auto shadow-lg flex flex-col lg:flex-row
         justify-center align-center'>
                <div className='m-2 p-2 flex flex-col justify-center items-center w-full lg:w-1/2 lg:block relative'>
                    <img src={logo} alt='logo' className='flex w-[120px] m-3' />
                    <img src={landingImg} alt='' className='hidden rounded-2xl lg:block lg:m-auto' />
                </div>
                <div className="m-3 p-2 lg:w-1/2 flex flex-col justify-center items-center">
                    <h1 className='text-2xl font-bold mb-4'>Login</h1>
                    <Input type='email' id='user' placeholder='Usuário' required onChange={(e)=>setEmail(e.target.value)}/>
                    <Input type='password' id='password' placeholder='Senha' onChange={(e)=> setPassword(e.target.value)} required/>
                    <Button text='Entrar' type='submit' onClick={handleSubmit}/>
                    <div className="mt-5 text-xs border-b border-[#9d1717] py-4 text-[#9d1717] w-full">
                        <a href="#">Esqueceu sua senha?</a>
                    </div>

                    <div className="mt-3 text-xs flex justify-between items-center">
                        <p>Ainda não tem cadastro? <a href='/cadastro'>Acesse aqui.</a></p>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default LandPage