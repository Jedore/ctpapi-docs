<p>获取短信验证码请求的回复</p>
<span class="anchor" id="1a696f95-318b-4e17-a438-935cd0a5d3bd"></span>
## 1.函数原型
<p>virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="03e12179-b104-42ce-bb2b-2eab687c1f9f"></span>
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
<span class="anchor" id="e1b7516d-414f-4434-b2d9-b5df28680d0c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="aff8bc7c-3cde-434e-abe4-09822516c6f4"></span>
## 4.FAQ
<p>无</p>
