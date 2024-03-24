<p>获取图形验证码请求的回复</p>
<span class="anchor" id="a3987a06-3512-4240-a307-9d466c8db5fb"></span>
## 1.函数原型
<p>virtual void OnRspGenUserCaptcha(CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="56750f5d-c009-4a74-bbd8-06b72621bccc"></span>
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
<span class="anchor" id="4f55fa2f-a983-46a4-af75-5a6f0d800cbd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="01cc664d-2260-4cf7-9c96-cb94ad68f22f"></span>
## 4.FAQ
<p>无</p>
