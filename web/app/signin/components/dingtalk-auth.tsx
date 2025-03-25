import React from 'react'
import { useRouter } from 'next/navigation'
import { useTranslation } from 'react-i18next'
import style from '../page.module.css'
import Button from '@/app/components/base/button'
import classNames from '@/utils/classnames'

type SocialAuthProps = {
  clientId: string
}

export default function DingTalkAuth(props: SocialAuthProps) {
  const { t } = useTranslation()
  const router = useRouter()

  /* Extend: start 钉钉快捷登录按钮 */
  const DingTalkCasLogin = () => {
    const params = new URLSearchParams()
    params.append('scope', 'openid')
    params.append('prompt', 'consent')
    params.append('response_type', 'code')
    params.append('client_id', props.clientId)
    params.append('redirect_uri', `${process.env.NEXT_PUBLIC_API_PREFIX}/ding-talk/third-party/login`)
    router.replace(`https://login.dingtalk.com/oauth2/auth?${params.toString()}`)
  }

  return <>
    <div className="mb-2">
      <a onClick={DingTalkCasLogin}>
        <Button
          className="w-full"
        >
          <span className={
            classNames(
              style.dingIcon,
              'w-5 h-5 mr-2',
            )
          }
          />
          <span className="truncate">{t('extend.sidebar.withDingTalk')}</span>
        </Button>
      </a>
    </div>
  </>
}
