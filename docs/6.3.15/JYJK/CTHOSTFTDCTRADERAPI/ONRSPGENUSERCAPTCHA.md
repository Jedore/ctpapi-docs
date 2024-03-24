<p>获取图形验证码请求的回复</p>
<span class="anchor" id="0908f2fe-ddc5-4ed7-9647-bdbf4fe47e3a"></span>
## 1.函数原型
<p>virtual void OnRspGenUserCaptcha(CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5ab76d03-1b4b-4d7e-88c3-66cdd41a605e"></span>
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
<span class="anchor" id="b5dbc580-e905-46b7-8c63-0d18c3b522f0"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3b82ffcc-9c2c-4548-acc3-e144d4203e99"></span>
## 4.FAQ
<p>无</p>
