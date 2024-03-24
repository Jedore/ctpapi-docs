<p>获取短信验证码请求的回复</p>
<span class="anchor" id="1d15dcde-19f5-4630-a1dc-ff9c42cb5001"></span>
## 1.函数原型
<p>virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a2d022eb-4464-4120-a6bf-e7bbedf71895"></span>
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
<span class="anchor" id="46d2e0ac-7d2f-42e9-9c53-5863df541bbd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="dbe47a56-0468-4b7f-ae0e-0537dba206df"></span>
## 4.FAQ
<p>无</p>
