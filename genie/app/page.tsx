import TopBar from './components/TopBar'
import LeftTrix from './components/LeftTrix'
import RightTrix from './components/RightTrix'

export default function Home() {
  return (
    <main>
      <TopBar />
      <div id = "body" className = "flex justify-content-center">
        <LeftTrix />
        <RightTrix />
      </div>
    </main>
  );
}