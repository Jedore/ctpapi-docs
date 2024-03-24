<p>获取短信验证码请求的回复</p>
<span class="anchor" id="b7cd16ee-6ab7-454b-b0da-4bc16c830911"></span>
## 1.函数原型
<p>virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2ac03907-cf0a-4bc9-86f2-b41cc9afe8dc"></span>
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
<span class="anchor" id="71187ca0-30f3-4489-aee0-cfc42f23f7fc"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="98aa2d4f-171a-4167-bf06-304f56e6420c"></span>
## 4.FAQ
<p>无</p>
