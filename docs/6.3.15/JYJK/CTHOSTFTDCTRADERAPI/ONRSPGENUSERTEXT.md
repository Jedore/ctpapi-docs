<p>获取短信验证码请求的回复</p>
<span class="anchor" id="22c81912-f8c3-48e8-89b1-a03d1dd7cbf7"></span>
## 1.函数原型
<p>virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="08527ad7-8bc6-4025-a45d-4046abea1c6d"></span>
## 2.参数
<p>pRspGenUserText：短信验证码生成的回复息</p>
<pre><code>struct CThostFtdcRspGenUserTextField
{
    ///短信验证码序号
    TThostFtdcUserTextSeqType UserTextSeq;
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
<span class="anchor" id="d88acfb3-bdb2-49f3-a3b0-39b3ce3aa7f0"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c5289ef6-a6f9-45cd-bccb-397ac656592b"></span>
## 4.FAQ
<p>无</p>
