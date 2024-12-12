<p>获取短信验证码请求的回复</p>
<span class="anchor" id="14e4f4b1-603f-45a5-a956-294760bdb34a"></span>
## 1.函数原型
<p>virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8578c7c8-3b6a-4093-8662-80bfd2b46317"></span>
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
<span class="anchor" id="40b03485-700d-4bba-b09e-1e4c78d6a2d0"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6410048b-e863-499e-8767-1744fdbe6a39"></span>
## 4.FAQ
<p>无</p>
