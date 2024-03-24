<p>获取图形验证码请求的回复</p>
<span class="anchor" id="e138ba32-72bd-4a84-a1f4-53c623af151a"></span>
## 1.函数原型
<p>virtual void OnRspGenUserCaptcha(CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="c466b601-a6f7-4cbd-8791-52fd24e2b6be"></span>
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
<span class="anchor" id="60eb3a68-d574-453f-b56e-8d920b5fbe0d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="41d4cffc-254f-4e85-bf67-7444905b6072"></span>
## 4.FAQ
<p>无</p>
