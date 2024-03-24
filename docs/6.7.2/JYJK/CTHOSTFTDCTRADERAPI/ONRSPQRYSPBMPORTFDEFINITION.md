<p>请求SPBM组合保证金套餐查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINTERPARAMETER/">ReqQrySPBMInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="63395316-3aab-4f9f-a10e-22102dbc43d5"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMPortfDefinition(CThostFtdcSPBMPortfDefinitionField *pSPBMPortfDefinition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="422d2c31-f3db-41ce-9d05-f13bc68236a0"></span>
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
<span class="anchor" id="924bde49-0ddc-42d0-8860-2c35a8fe6883"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e594f4eb-9d5d-4e88-be71-6eb95ed05732"></span>
## 4.FAQ
<p>无</p>
