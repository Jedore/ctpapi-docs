<p>订阅询价应答，当调用SubscribeForQuoteRsp后，通过此接口返回。</p>
<span class="anchor" id="f1514751-47ea-49e4-bd00-d639d21d1a19"></span>
## 1.函数原型
<p>virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="c78b33e8-a867-48c5-ad87-c9c3acbe817a"></span>
## 2.参数
<p>pSpecificInstrument：指定的合约</p>
<pre><code>struct CThostFtdcSpecificInstrumentField
{
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
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
<span class="anchor" id="78727d4d-a72d-4986-aad5-4f520ff25fb5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="aedee483-ef7f-4c88-86bb-88801d40d9ef"></span>
## 4.FAQ
<p>无</p>
