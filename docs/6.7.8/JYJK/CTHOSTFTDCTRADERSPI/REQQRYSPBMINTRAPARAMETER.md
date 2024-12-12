<p>请求SPBM品种内对锁仓折扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINTRAPARAMETER/">OnRspQrySPBMIntraParameter</a></p>
<span class="anchor" id="0ce84552-d0d6-43d0-8bc8-781f588179a2"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMIntraParameter(CThostFtdcQrySPBMIntraParameterField *pQrySPBMIntraParameter, int nRequestID) = 0;</p>
<span class="anchor" id="43afdf9f-2451-4a01-b2fe-d8dedb635506"></span>
## 2.参数
<p>pQrySPBMIntraParameter：SPBM品种内对锁仓折扣参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="bb1daae2-b4bc-4b01-bcfa-fe7ea49ca5a2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0200b76e-0673-4e9d-b878-06bea45c293c"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="6f3db438-e7fe-4570-bc9f-d8663a23db94"></span>
## 5.FAQ
<p>无</p>
