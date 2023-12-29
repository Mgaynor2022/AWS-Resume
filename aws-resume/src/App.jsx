import { useState } from 'react'
import Header from './Header'
import './App.css'
import Projects from './Projects'
import WorkExperience from './Experience'
import Education from './Education'

function App() {

  return (
    <>
      <Header />
      <Projects />
      <WorkExperience />
      <Education />
    </>
  )
}

export default App
