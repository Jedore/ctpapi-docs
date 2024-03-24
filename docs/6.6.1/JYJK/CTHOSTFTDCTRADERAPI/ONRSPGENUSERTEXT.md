<p>获取短信验证码请求的回复</p>
<span class="anchor" id="eec55831-d7b4-41a6-8db5-2c679f14aec9"></span>
## 1.函数原型
<p>virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="34e47922-c295-4656-94a2-8fb34fed07bb"></span>
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
<span class="anchor" id="c6f974cd-3d87-4e25-97d3-b4b6bc0855bf"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6851fbae-0927-4f22-b9a3-b1d810b4d78e"></span>
## 4.FAQ
<p>无</p>
