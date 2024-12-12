<p>请求SPBM组合保证金套餐查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTERPARAMETER/">ReqQrySPBMInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="1ee4dc67-6b21-49eb-a93d-ae8af26fc727"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMPortfDefinition(CThostFtdcSPBMPortfDefinitionField *pSPBMPortfDefinition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e51e169a-0dc7-49cd-9c8c-2bbd92fa53f9"></span>
## 2.参数
<p>pSPBMPortfDefinition：组合保证金套餐</p>
<pre><code>struct CThostFtdcSPBMPortfDefinitionField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///组合保证金套餐代码
    TThostFtdcPortfolioDefIDType    PortfolioDefID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
    ///是否启用SPBM
    TThostFtdcBoolType  IsSPBM;
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
<span class="anchor" id="f0c1fb4c-f1ce-4860-9077-607495817d67"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="267af6cf-b864-42e4-8638-2cfc914df237"></span>
## 4.FAQ
<p>无</p>
