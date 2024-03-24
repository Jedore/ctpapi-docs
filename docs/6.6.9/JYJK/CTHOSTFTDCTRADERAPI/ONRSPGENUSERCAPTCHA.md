<p>获取图形验证码请求的回复</p>
<span class="anchor" id="12978d5b-4f8e-429c-881d-e22294abcf32"></span>
## 1.函数原型
<p>virtual void OnRspGenUserCaptcha(CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5e9685cc-5d48-48ff-9db2-f501e26365dc"></span>
## 2.参数
<p>pRspGenUserCaptcha：生成的图片验证码信息</p>
<pre><code>struct CThostFtdcRspGenUserCaptchaField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///图片信息长度
    TThostFtdcCaptchaInfoLenType CaptchaInfoLen;
    ///图片信息
    TThostFtdcCaptchaInfoType CaptchaInfo;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="7fb2d557-2763-4ebe-875a-f5aea58c15cc"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="772b31d1-44cc-4ec6-9ec9-65522a1d0f93"></span>
## 4.FAQ
<p>无</p>
