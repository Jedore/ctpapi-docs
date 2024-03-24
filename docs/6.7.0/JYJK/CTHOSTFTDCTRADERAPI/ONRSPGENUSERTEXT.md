<p>获取短信验证码请求的回复</p>
<span class="anchor" id="4000009a-1af7-47bc-92f0-881affb0898d"></span>
## 1.函数原型
<p>virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2756b575-b7c0-4983-9d9e-580de4672869"></span>
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
<span class="anchor" id="70a1a796-bf94-4d91-affe-41984b580455"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3a1458be-7225-46a6-831f-788f994a25fb"></span>
## 4.FAQ
<p>无</p>
