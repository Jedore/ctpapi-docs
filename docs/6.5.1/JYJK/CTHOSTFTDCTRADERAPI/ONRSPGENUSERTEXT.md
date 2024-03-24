<p>获取短信验证码请求的回复</p>
<span class="anchor" id="6cba5100-b5b0-4568-8f60-a69a562be60f"></span>
## 1.函数原型
<p>virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="98eb8e81-bf07-4309-b3f6-fdf244c666d5"></span>
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
<span class="anchor" id="17f94eb0-8b4b-491f-9505-84d58a4288e1"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="63e169f5-edee-45d5-9236-8ee028251965"></span>
## 4.FAQ
<p>无</p>
