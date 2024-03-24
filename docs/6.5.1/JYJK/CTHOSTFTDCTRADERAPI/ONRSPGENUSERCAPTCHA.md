<p>获取图形验证码请求的回复</p>
<span class="anchor" id="130eb598-ac90-490e-aaf4-765a0dc140c1"></span>
## 1.函数原型
<p>virtual void OnRspGenUserCaptcha(CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="3840ab6f-5bdb-42b8-83e9-438931498b14"></span>
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
<span class="anchor" id="759da4c4-ed22-4e54-95a0-364118716147"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0cfef40b-0ab3-4331-82bd-8eb6429095d5"></span>
## 4.FAQ
<p>无</p>
