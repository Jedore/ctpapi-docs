<p>取消订阅行情应答，当UnSubscribeMarketData后，调用此接口。</p>
<span class="anchor" id="9f745fe6-97a9-4489-8fb7-10318aebe722"></span>
## 1.函数原型
<p>virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e3174caf-5ea2-40af-9cc4-7ce96ad288a0"></span>
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
<span class="anchor" id="23d03aa7-145e-4f60-95ae-7b4489b2a07a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5cbc09ae-13ac-4fb9-b29b-6f7ebaecd708"></span>
## 4.FAQ
<p>无</p>
