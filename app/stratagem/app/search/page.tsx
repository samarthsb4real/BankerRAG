import { Chat } from '@/components/chat'
import { redirect } from 'next/navigation'

export const maxDuration = 60

function generateId() {
    return Math.random().toString(36).substr(2, 9)
}

export default async function SearchPage(props: {
    searchParams: Promise<{ q: string }>
}) {
    const { q } = await props.searchParams
    if (!q) {
        redirect('/')
    }

    const id = generateId()
    return <Chat id={id} query={q} />
}