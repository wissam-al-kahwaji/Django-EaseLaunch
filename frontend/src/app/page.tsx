import Image from "next/image";

export default function Home() {
  return (
    <main className="flex items-center justify-center h-screen">
    <a href="https://github.com/caodlly/octo-launch">
    <div>
      <Image
          src="/octo.svg"
          alt="Octo Logo"
          width={200}
          height={80}
          priority
          />
      <div className="text-xl font-semibold text-right">
      octo-launch
      </div>
    </div>
          </a>
    </main>
  );
}
