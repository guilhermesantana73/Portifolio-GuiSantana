import logo from '../assets/whiteLogo.svg'
import profile from '../assets/profile.svg'
const Navbar = () => {
  return (
    <nav className='flex bg-[#9d1717] justify-between'>
        <img src={logo} alt="Logo" className='m-2 p-2'/>
        <img src={profile} alt="Perfil" className='m-2 p-2'/>   
    </nav>
  )
}

export default Navbar