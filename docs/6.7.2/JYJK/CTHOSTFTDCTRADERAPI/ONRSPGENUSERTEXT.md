<p>获取短信验证码请求的回复</p>
<span class="anchor" id="e3b25fd4-9c07-41e3-ba08-46ea5ea9b381"></span>
## 1.函数原型
<p>virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a5dd39d7-9891-4697-ac12-ec171ceff1a0"></span>
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
<span class="anchor" id="51d5aa3b-b926-4eeb-8473-e6f0ba540874"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1e0d4b97-3cb6-4fb4-a9aa-18cd153de0db"></span>
## 4.FAQ
<p>无</p>
